<template>
  <div class="prompt-list">
    <div class="search-section">
      <h2>البحث في البرومبت - Search Prompts</h2>
      <div class="search-container">
        <input 
          v-model="searchQuery" 
          type="text" 
          placeholder="ابحث عن برومبت... Search for prompts..."
          class="search-input"
        />
        <button @click="searchPrompts" class="search-btn">بحث - Search</button>
      </div>
    </div>
    
    <div class="add-prompt-section">
      <h3>إضافة برومبت جديد - Add New Prompt</h3>
      <div class="prompt-form">
        <input 
          v-model="newPrompt.title" 
          type="text" 
          placeholder="عنوان البرومبت - Prompt Title"
          class="form-input"
        />
        <textarea 
          v-model="newPrompt.content" 
          placeholder="محتوى البرومبت - Prompt Content"
          class="form-textarea"
        ></textarea>
        <input 
          v-model="newPrompt.category" 
          type="text" 
          placeholder="الفئة - Category"
          class="form-input"
        />
        <button @click="addPrompt" class="add-btn">إضافة - Add Prompt</button>
      </div>
    </div>
    
    <div class="prompts-grid">
      <div v-for="prompt in filteredPrompts" :key="prompt.id" class="prompt-card">
        <h3 class="prompt-title">{{ prompt.title }}</h3>
        <p class="prompt-content">{{ prompt.content }}</p>
        <div class="prompt-meta">
          <span class="category">الفئة: {{ prompt.category }}</span>
          <span class="date">التاريخ: {{ prompt.date }}</span>
        </div>
        <button @click="copyPrompt(prompt.content)" class="copy-btn">نسخ - Copy</button>
      </div>
    </div>
    
    <div v-if="filteredPrompts.length === 0" class="no-prompts">
      <p>لا توجد برومبت متاحة - No prompts available</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PromptList',
  data() {
    return {
      searchQuery: '',
      prompts: [
        {
          id: 1,
          title: 'Creative Writing Assistant',
          content: 'Act as a creative writing assistant. Help me write a compelling story about...',
          category: 'Writing',
          date: '2025-01-01'
        },
        {
          id: 2,
          title: 'مساعد في البرمجة',
          content: 'أعمل كمطور برمجيات محترف. ساعدني في كتابة كود...',
          category: 'برمجة',
          date: '2025-01-02'
        }
      ],
      newPrompt: {
        title: '',
        content: '',
        category: ''
      }
    }
  },
  computed: {
    filteredPrompts() {
      if (!this.searchQuery) return this.prompts
      return this.prompts.filter(prompt => 
        prompt.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
        prompt.content.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
        prompt.category.toLowerCase().includes(this.searchQuery.toLowerCase())
      )
    }
  },
  methods: {
    searchPrompts() {
      // Search is handled by computed property
      console.log('Searching for:', this.searchQuery)
    },
    addPrompt() {
      if (this.newPrompt.title && this.newPrompt.content) {
        const prompt = {
          id: Date.now(),
          title: this.newPrompt.title,
          content: this.newPrompt.content,
          category: this.newPrompt.category || 'General',
          date: new Date().toISOString().split('T')[0]
        }
        this.prompts.unshift(prompt)
        this.newPrompt = { title: '', content: '', category: '' }
        alert('تم إضافة البرومبت بنجاح - Prompt added successfully!')
      } else {
        alert('يرجى ملء جميع الحقول المطلوبة - Please fill in all required fields')
      }
    },
    copyPrompt(content) {
      navigator.clipboard.writeText(content).then(() => {
        alert('تم نسخ البرومبت - Prompt copied to clipboard!')
      })
    }
  }
}
</script>

<style scoped>
.prompt-list {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.search-section {
  margin-bottom: 2rem;
  text-align: center;
}

.search-section h2 {
  color: #333;
  margin-bottom: 1rem;
}

.search-container {
  display: flex;
  gap: 10px;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

.search-input {
  padding: 12px;
  border: 2px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
  min-width: 300px;
}

.search-btn {
  padding: 12px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
}

.add-prompt-section {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 2rem;
}

.add-prompt-section h3 {
  margin-bottom: 1rem;
  color: #333;
}

.prompt-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.form-input, .form-textarea {
  padding: 12px;
  border: 2px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
}

.form-textarea {
  min-height: 100px;
  resize: vertical;
}

.add-btn {
  padding: 12px;
  background: #28a745;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
}

.prompts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 2rem;
}

.prompt-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.prompt-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.prompt-title {
  margin: 0 0 10px 0;
  color: #333;
  font-size: 1.2em;
}

.prompt-content {
  color: #666;
  line-height: 1.5;
  margin-bottom: 15px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.prompt-meta {
  display: flex;
  justify-content: space-between;
  font-size: 0.9em;
  color: #888;
  margin-bottom: 15px;
}

.category {
  background: #e3f2fd;
  padding: 4px 8px;
  border-radius: 4px;
}

.copy-btn {
  width: 100%;
  padding: 10px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.copy-btn:hover {
  background: #0056b3;
}

.no-prompts {
  text-align: center;
  padding: 2rem;
  color: #666;
  font-size: 1.1em;
}

@media (max-width: 768px) {
  .search-container {
    flex-direction: column;
  }
  
  .search-input {
    min-width: 100%;
  }
  
  .prompts-grid {
    grid-template-columns: 1fr;
  }
}
</style>
