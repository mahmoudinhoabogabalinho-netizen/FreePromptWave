# FreePromptWave Backend 🔧

## API Server Documentation | توثيق خادم API

### 🏗️ Architecture Overview | نظرة عامة على الهندسة المعمارية

FreePromptWave backend is built with Flask and designed with **Zero Data, Zero Logging, No Liability** principles.

خادم FreePromptWave مبني بـ Flask ومصمم بمبادئ **عدم جمع البيانات، عدم التسجيل، بدون مسؤولية**.

### 📋 Current Features | الميزات الحالية

- ✅ RESTful API endpoints for prompt management
- ✅ CORS enabled for frontend integration  
- ✅ JSON file-based storage (local)
- ✅ Bilingual Arabic/English support
- ✅ Search and categorization functionality
- ✅ Privacy-first design

### 🔒 Security & Encryption Documentation

#### Current Status | الحالة الحالية
**⚠️ ENCRYPTION HANDLER: NOT IMPLEMENTED**

The current implementation uses **plain JSON storage** without encryption. This is intentional for the current "Zero Data" policy:

- Data stored locally only
- No sensitive personal information collected
- No external data transmission
- Complete transparency for open source review

#### 🚀 Future Encryption Implementation Plan

For enhanced security in future versions, the following encryption handler should be implemented:

```python
# ENCRYPTION HANDLER DOCUMENTATION POINTER
# File: backend/security/encryption_handler.py (NOT YET IMPLEMENTED)

class EncryptionHandler:
    """
    Future encryption handler for sensitive data protection
    
    Features to implement:
    - AES-256 encryption for prompt content
    - Key rotation mechanism
    - Salt-based password hashing
    - Secure key storage
    - GDPR compliance utilities
    """
    
    def encrypt_prompt_content(self, content: str) -> str:
        """Encrypt prompt content before storage"""
        pass
    
    def decrypt_prompt_content(self, encrypted_content: str) -> str:
        """Decrypt prompt content for retrieval"""
        pass
    
    def generate_secure_key(self) -> str:
        """Generate cryptographically secure keys"""
        pass
```

#### 📖 Implementation References

**For future development:**
- Use Python `cryptography` library
- Implement Fernet symmetric encryption
- Add environment-based key management
- Consider HashiCorp Vault for production
- Follow OWASP security guidelines

**Dependencies to add:**
```bash
pip install cryptography python-dotenv
```

### 🌐 API Endpoints | نقاط النهاية

#### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/api/prompts` | Get all prompts |
| POST | `/api/prompts` | Add new prompt |
| GET | `/api/prompts/search` | Search prompts |
| GET | `/api/prompts/<id>` | Get specific prompt |
| POST | `/api/prompts/<id>/like` | Like a prompt |
| GET | `/api/categories` | Get all categories |

### 🚀 Getting Started | البدء

#### Prerequisites
- Python 3.8+
- pip (Python package manager)

#### Installation

```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

#### Configuration

- **Host:** `0.0.0.0` (all interfaces)
- **Port:** `5000`
- **Debug:** `True` (development only)
- **Storage:** `prompts_store.json`

### 📁 Project Structure | هيكل المشروع

```
backend/
├── app.py                 # Main Flask application
├── prompts_store.json     # JSON data storage
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
└── security/             # (Future) Security modules
    └── encryption_handler.py  # (NOT YET IMPLEMENTED)
```

### 🔧 Development Guidelines | إرشادات التطوير

#### Code Standards
- Follow PEP 8 Python style guide
- Use type hints where appropriate
- Maintain bilingual comments (Arabic/English)
- Ensure Zero Data compliance

#### Testing
```bash
# Test API endpoints
curl http://localhost:5000/api/prompts

# Test with Arabic content
curl -X POST http://localhost:5000/api/prompts \
  -H "Content-Type: application/json" \
  -d '{"title": "اختبار", "content": "محتوى تجريبي"}'
```

### 📊 Privacy & Compliance | الخصوصية والامتثال

#### Zero Data Policy
- No user tracking or analytics
- No external API calls
- No logging of personal information
- Local storage only
- No cookies or session tracking

#### Future Compliance Features
- GDPR deletion requests
- Data export functionality
- Audit logging (optional)
- Encryption at rest

### 🐛 Troubleshooting | استكشاف الأخطاء

#### Common Issues

1. **Port already in use**
   ```bash
   # Find process using port 5000
   lsof -i :5000
   # Kill the process
   kill -9 <PID>
   ```

2. **CORS errors**
   - Ensure Flask-CORS is installed
   - Check frontend URL configuration

3. **JSON file permissions**
   ```bash
   chmod 644 prompts_store.json
   ```

### 📞 Support & Contributing | الدعم والمساهمة

- **Issues:** Use GitHub Issues for bug reports
- **Security:** Report security issues privately
- **Contributing:** Follow the project's contribution guidelines
- **License:** MIT License

---

**⚠️ Security Notice:** This backend currently operates under a "Zero Data" policy with no encryption. For production use with sensitive data, implement the encryption handler as documented above.

**إشعار أمني:** هذا الخادم يعمل حالياً تحت سياسة "عدم جمع البيانات" بدون تشفير. للاستخدام في الإنتاج مع البيانات الحساسة، قم بتنفيذ معالج التشفير كما هو موثق أعلاه.
