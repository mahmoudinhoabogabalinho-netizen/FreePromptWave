from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

# File to store prompts
PROMPTS_FILE = 'prompts_store.json'

def load_prompts():
    """Load prompts from JSON file"""
    if os.path.exists(PROMPTS_FILE):
        try:
            with open(PROMPTS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_prompts(prompts):
    """Save prompts to JSON file"""
    with open(PROMPTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """Serve main page"""
    return {
        "message": "مرحباً بكم في موجة البرومبت المجانية - Welcome to FreePromptWave!",
        "description": "منصة مشاركة البرومبت المجانية مفتوحة المصدر - Free Open Source AI Prompt Sharing Platform",
        "version": "1.0.0",
        "endpoints": {
            "GET /api/prompts": "الحصول على جميع البرومبت - Get all prompts",
            "POST /api/prompts": "إضافة برومبت جديد - Add new prompt",
            "GET /api/prompts/search": "البحث في البرومبت - Search prompts"
        }
    }

@app.route('/api/prompts', methods=['GET'])
def get_prompts():
    """Get all prompts"""
    prompts = load_prompts()
    return jsonify({
        'success': True,
        'data': prompts,
        'total': len(prompts)
    })

@app.route('/api/prompts', methods=['POST'])
def add_prompt():
    """Add a new prompt"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or not data.get('title') or not data.get('content'):
            return jsonify({
                'success': False,
                'message': 'العنوان والمحتوى مطلوبان - Title and content are required'
            }), 400
        
        # Load existing prompts
        prompts = load_prompts()
        
        # Create new prompt
        new_prompt = {
            'id': len(prompts) + 1,
            'title': data['title'],
            'content': data['content'],
            'category': data.get('category', 'عام - General'),
            'tags': data.get('tags', []),
            'author': data.get('author', 'مجهول - Anonymous'),
            'date_created': datetime.now().isoformat(),
            'likes': 0,
            'views': 0
        }
        
        # Add to prompts list
        prompts.append(new_prompt)
        
        # Save to file
        save_prompts(prompts)
        
        return jsonify({
            'success': True,
            'message': 'تم إضافة البرومبت بنجاح - Prompt added successfully!',
            'data': new_prompt
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'خطأ في الخادم - Server error: {str(e)}'
        }), 500

@app.route('/api/prompts/search', methods=['GET'])
def search_prompts():
    """Search prompts by query"""
    query = request.args.get('q', '').lower()
    category = request.args.get('category', '')
    
    prompts = load_prompts()
    filtered_prompts = []
    
    for prompt in prompts:
        # Search in title, content, and category
        if (query in prompt['title'].lower() or 
            query in prompt['content'].lower() or
            query in prompt['category'].lower()):
            
            # Filter by category if specified
            if not category or category.lower() in prompt['category'].lower():
                filtered_prompts.append(prompt)
    
    return jsonify({
        'success': True,
        'data': filtered_prompts,
        'total': len(filtered_prompts),
        'query': query,
        'category': category
    })

@app.route('/api/prompts/<int:prompt_id>', methods=['GET'])
def get_prompt(prompt_id):
    """Get a specific prompt by ID"""
    prompts = load_prompts()
    
    for prompt in prompts:
        if prompt['id'] == prompt_id:
            # Increment view count
            prompt['views'] += 1
            save_prompts(prompts)
            return jsonify({
                'success': True,
                'data': prompt
            })
    
    return jsonify({
        'success': False,
        'message': 'البرومبت غير موجود - Prompt not found'
    }), 404

@app.route('/api/prompts/<int:prompt_id>/like', methods=['POST'])
def like_prompt(prompt_id):
    """Like a prompt"""
    prompts = load_prompts()
    
    for prompt in prompts:
        if prompt['id'] == prompt_id:
            prompt['likes'] += 1
            save_prompts(prompts)
            return jsonify({
                'success': True,
                'message': 'تم الإعجاب بالبرومبت - Prompt liked!',
                'likes': prompt['likes']
            })
    
    return jsonify({
        'success': False,
        'message': 'البرومبت غير موجود - Prompt not found'
    }), 404

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Get all unique categories"""
    prompts = load_prompts()
    categories = list(set(prompt['category'] for prompt in prompts))
    
    return jsonify({
        'success': True,
        'data': categories,
        'total': len(categories)
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'message': 'الصفحة غير موجودة - Page not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'message': 'خطأ في الخادم - Internal server error'
    }), 500

if __name__ == '__main__':
    # Create prompts file if it doesn't exist
    if not os.path.exists(PROMPTS_FILE):
        save_prompts([])
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
