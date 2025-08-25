<template>
  <div class="smart-prompt-maker">
    <!-- UI لصانع البرومبت الذكي -->
    <div class="prompt-maker-header">
      <h2>🧠 صانع البرومبت الذكي | Smart Prompt Maker</h2>
      <p class="description">إنشاء وتحسين البرومبت بذكاء اصطناعي | AI-Powered Prompt Creation</p>
    </div>
    
    <div class="prompt-input-section">
      <label for="prompt-input">أدخل فكرة البرومبت | Enter Prompt Idea:</label>
      <textarea 
        id="prompt-input"
        v-model="promptIdea"
        placeholder="مثال: اكتب قصة قصيرة عن المستقبل..."
        class="prompt-textarea"
        rows="4"
      ></textarea>
    </div>
    
    <div class="controls-section">
      <button @click="generateSmartPrompt" class="generate-btn" :disabled="!promptIdea.trim()">
        🚀 إنشاء برومبت ذكي | Generate Smart Prompt
      </button>
      <button @click="clearAll" class="clear-btn">
        🗑️ مسح | Clear
      </button>
    </div>
    
    <div v-if="generatedPrompt" class="output-section">
      <label>البرومبت المحسّن | Enhanced Prompt:</label>
      <div class="generated-prompt">
        {{ generatedPrompt }}
      </div>
      <div class="output-controls">
        <button @click="copyPrompt" class="copy-btn">
          📋 نسخ | Copy
        </button>
        <button @click="savePrompt" class="save-btn">
          💾 حفظ | Save
        </button>
      </div>
    </div>
    
    <div v-if="showSuccess" class="success-message">
      ✅ تم النسخ بنجاح | Copied Successfully!
    </div>
  </div>
</template>

<script>
export default {
  name: 'SmartPromptMaker',
  data() {
    return {
      promptIdea: '',
      generatedPrompt: '',
      showSuccess: false
    }
  },
  methods: {
    generateSmartPrompt() {
      if (!this.promptIdea.trim()) return;
      
      // تحسين البرومبت بإضافة سياق وتوجيهات واضحة
      const enhancedPrompt = this.enhancePrompt(this.promptIdea);
      this.generatedPrompt = enhancedPrompt;
    },
    
    enhancePrompt(originalPrompt) {
      // خوارزمية تحسين البرومبت المحلية (بدون إرسال بيانات خارجية)
      const prefixes = [
        'تصرف كخبير في ',
        'اكتب بشكل مفصل ومهني عن ',
        'قدم تحليلاً شاملاً لـ ',
        'اشرح بطريقة واضحة ومنظمة '
      ];
      
      const suffixes = [
        '. تأكد من تضمين أمثلة عملية وتفاصيل مفيدة.',
        '. استخدم أسلوباً واضحاً ومنظماً في العرض.',
        '. قدم معلومات دقيقة ومحدثة.',
        '. اجعل المحتوى مفيداً وقابلاً للتطبيق.'
      ];
      
      const randomPrefix = prefixes[Math.floor(Math.random() * prefixes.length)];
      const randomSuffix = suffixes[Math.floor(Math.random() * suffixes.length)];
      
      return `${randomPrefix}${originalPrompt}${randomSuffix}`;
    },
    
    copyPrompt() {
      if (navigator.clipboard && this.generatedPrompt) {
        navigator.clipboard.writeText(this.generatedPrompt)
          .then(() => {
            this.showSuccessMessage();
          })
          .catch(() => {
            // Fallback for older browsers
            this.fallbackCopy();
          });
      } else {
        this.fallbackCopy();
      }
    },
    
    fallbackCopy() {
      const textArea = document.createElement('textarea');
      textArea.value = this.generatedPrompt;
      document.body.appendChild(textArea);
      textArea.select();
      document.execCommand('copy');
      document.body.removeChild(textArea);
      this.showSuccessMessage();
    },
    
    showSuccessMessage() {
      this.showSuccess = true;
      setTimeout(() => {
        this.showSuccess = false;
      }, 2000);
    },
    
    savePrompt() {
      if (this.generatedPrompt) {
        // حفظ محلي في localStorage (بدون إرسال بيانات خارجية)
        const savedPrompts = JSON.parse(localStorage.getItem('freePromptWave_savedPrompts') || '[]');
        const newPrompt = {
          id: Date.now(),
          original: this.promptIdea,
          enhanced: this.generatedPrompt,
          timestamp: new Date().toISOString()
        };
        
        savedPrompts.push(newPrompt);
        localStorage.setItem('freePromptWave_savedPrompts', JSON.stringify(savedPrompts));
        
        this.$emit('prompt-saved', newPrompt);
        this.showSuccessMessage();
      }
    },
    
    clearAll() {
      this.promptIdea = '';
      this.generatedPrompt = '';
      this.showSuccess = false;
    }
  }
}
</script>

<style scoped>
.smart-prompt-maker {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 15px;
  color: white;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.prompt-maker-header {
  text-align: center;
  margin-bottom: 30px;
}

.prompt-maker-header h2 {
  font-size: 2rem;
  margin-bottom: 10px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.description {
  opacity: 0.9;
  font-size: 1.1rem;
}

.prompt-input-section {
  margin-bottom: 20px;
}

.prompt-input-section label {
  display: block;
  margin-bottom: 10px;
  font-weight: bold;
  font-size: 1.1rem;
}

.prompt-textarea {
  width: 100%;
  padding: 15px;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-family: inherit;
  resize: vertical;
  background: rgba(255, 255, 255, 0.95);
  color: #333;
  box-sizing: border-box;
}

.prompt-textarea:focus {
  outline: none;
  box-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
}

.controls-section {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;
  flex-wrap: wrap;
}

.generate-btn, .clear-btn, .copy-btn, .save-btn {
  padding: 12px 24px;
  border: none;
  border-radius: 25px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
}

.generate-btn {
  background: linear-gradient(45deg, #4CAF50, #45a049);
  color: white;
  flex: 1;
}

.generate-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
}

.generate-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.clear-btn {
  background: linear-gradient(45deg, #f44336, #da190b);
  color: white;
}

.clear-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(244, 67, 54, 0.4);
}

.output-section {
  background: rgba(255, 255, 255, 0.1);
  padding: 20px;
  border-radius: 10px;
  margin-bottom: 20px;
}

.output-section label {
  display: block;
  margin-bottom: 15px;
  font-weight: bold;
  font-size: 1.1rem;
}

.generated-prompt {
  background: rgba(255, 255, 255, 0.95);
  color: #333;
  padding: 20px;
  border-radius: 10px;
  margin-bottom: 15px;
  line-height: 1.6;
  font-size: 1rem;
  min-height: 100px;
  white-space: pre-wrap;
}

.output-controls {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.copy-btn {
  background: linear-gradient(45deg, #2196F3, #0b7dda);
  color: white;
  flex: 1;
}

.copy-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(33, 150, 243, 0.4);
}

.save-btn {
  background: linear-gradient(45deg, #FF9800, #e68900);
  color: white;
  flex: 1;
}

.save-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(255, 152, 0, 0.4);
}

.success-message {
  background: linear-gradient(45deg, #4CAF50, #45a049);
  color: white;
  padding: 15px;
  border-radius: 10px;
  text-align: center;
  font-weight: bold;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .smart-prompt-maker {
    padding: 15px;
  }
  
  .prompt-maker-header h2 {
    font-size: 1.5rem;
  }
  
  .controls-section {
    flex-direction: column;
  }
  
  .output-controls {
    flex-direction: column;
  }
}

/* Privacy Compliance - Zero Data Policy */
/* هذا المكون يلتزم بسياسة Zero Data - لا يرسل أي بيانات خارجية */
/* This component complies with Zero Data policy - no external data transmission */
</style>
