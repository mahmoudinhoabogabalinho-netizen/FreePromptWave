<template>
  <div class="fancy-prompt-generator">
    <div class="container">
      <div class="header">
        <h1 class="title">🎨 Fancy Prompt Generator</h1>
        <p class="subtitle">Create amazing AI prompts with style</p>
      </div>
      
      <div class="input-section">
        <div class="input-group">
          <label for="topic" class="label">Topic:</label>
          <input 
            id="topic"
            v-model="topic" 
            type="text" 
            placeholder="Enter your topic (e.g., 'mountain landscape')"
            class="input"
          />
        </div>
        
        <div class="input-group">
          <label for="style" class="label">Style:</label>
          <select id="style" v-model="selectedStyle" class="select">
            <option value="">Choose a style...</option>
            <option v-for="style in styles" :key="style" :value="style">
              {{ style }}
            </option>
          </select>
        </div>
        
        <div class="input-group">
          <label for="mood" class="label">Mood:</label>
          <select id="mood" v-model="selectedMood" class="select">
            <option value="">Choose a mood...</option>
            <option v-for="mood in moods" :key="mood" :value="mood">
              {{ mood }}
            </option>
          </select>
        </div>
        
        <div class="input-group">
          <label for="quality" class="label">Quality Level:</label>
          <select id="quality" v-model="selectedQuality" class="select">
            <option value="">Choose quality...</option>
            <option v-for="quality in qualities" :key="quality" :value="quality">
              {{ quality }}
            </option>
          </select>
        </div>
      </div>
      
      <div class="button-section">
        <button 
          @click="generatePrompt" 
          :disabled="!topic"
          class="generate-btn"
        >
          ✨ Generate Fancy Prompt
        </button>
        
        <button 
          @click="clearAll" 
          class="clear-btn"
        >
          🗑️ Clear All
        </button>
      </div>
      
      <div v-if="generatedPrompt" class="result-section">
        <h3 class="result-title">Generated Prompt:</h3>
        <div class="prompt-box">
          <p class="prompt-text">{{ generatedPrompt }}</p>
          <button @click="copyPrompt" class="copy-btn">
            {{ copied ? '✅ Copied!' : '📋 Copy' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FancyPromptGenerator',
  data() {
    return {
      topic: '',
      selectedStyle: '',
      selectedMood: '',
      selectedQuality: '',
      generatedPrompt: '',
      copied: false,
      styles: [
        'Photorealistic',
        'Digital Art',
        'Oil Painting',
        'Watercolor',
        'Sketch',
        'Anime Style',
        'Cartoon',
        '3D Render',
        'Vintage',
        'Minimalist',
        'Abstract',
        'Surreal'
      ],
      moods: [
        'Peaceful',
        'Dramatic',
        'Mysterious',
        'Joyful',
        'Melancholic',
        'Energetic',
        'Serene',
        'Dark',
        'Bright',
        'Romantic',
        'Epic',
        'Cozy'
      ],
      qualities: [
        'High Quality',
        '4K Resolution',
        '8K Ultra HD',
        'Professional Photography',
        'Studio Lighting',
        'Cinematic',
        'Award Winning',
        'Masterpiece',
        'Highly Detailed',
        'Sharp Focus'
      ]
    }
  },
  methods: {
    generatePrompt() {
      if (!this.topic) {
        alert('Please enter a topic first!');
        return;
      }
      
      let prompt = this.topic;
      
      if (this.selectedStyle) {
        prompt += `, ${this.selectedStyle} style`;
      }
      
      if (this.selectedMood) {
        prompt += `, ${this.selectedMood.toLowerCase()} mood`;
      }
      
      if (this.selectedQuality) {
        prompt += `, ${this.selectedQuality.toLowerCase()}`;
      }
      
      // Add some creative enhancements
      const enhancements = [
        'beautiful composition',
        'perfect lighting',
        'trending on artstation',
        'highly detailed',
        'vibrant colors'
      ];
      
      const randomEnhancement = enhancements[Math.floor(Math.random() * enhancements.length)];
      prompt += `, ${randomEnhancement}`;
      
      this.generatedPrompt = prompt;
    },
    
    clearAll() {
      this.topic = '';
      this.selectedStyle = '';
      this.selectedMood = '';
      this.selectedQuality = '';
      this.generatedPrompt = '';
      this.copied = false;
    },
    
    copyPrompt() {
      if (navigator.clipboard) {
        navigator.clipboard.writeText(this.generatedPrompt).then(() => {
          this.copied = true;
          setTimeout(() => {
            this.copied = false;
          }, 2000);
        });
      } else {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = this.generatedPrompt;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        this.copied = true;
        setTimeout(() => {
          this.copied = false;
        }, 2000);
      }
    }
  }
}
</script>

<style scoped>
.fancy-prompt-generator {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2rem;
  font-family: 'Arial', sans-serif;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  backdrop-filter: blur(10px);
}

.header {
  background: linear-gradient(135deg, #ff6b6b, #ffa726);
  padding: 3rem 2rem;
  text-align: center;
  color: white;
}

.title {
  font-size: 2.5rem;
  margin: 0 0 0.5rem 0;
  font-weight: 700;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.subtitle {
  font-size: 1.2rem;
  margin: 0;
  opacity: 0.9;
}

.input-section {
  padding: 2rem;
  display: grid;
  gap: 1.5rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.label {
  font-weight: 600;
  color: #333;
  font-size: 1rem;
}

.input,
.select {
  padding: 0.75rem;
  border: 2px solid #e1e5e9;
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: white;
}

.input:focus,
.select:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
  transform: translateY(-1px);
}

.button-section {
  padding: 0 2rem 2rem;
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.generate-btn {
  flex: 1;
  min-width: 200px;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #4caf50, #45a049);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.generate-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(76, 175, 80, 0.3);
}

.generate-btn:disabled {
  background: #cccccc;
  cursor: not-allowed;
  transform: none;
}

.clear-btn {
  padding: 1rem 1.5rem;
  background: linear-gradient(135deg, #f44336, #d32f2f);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.clear-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(244, 67, 54, 0.3);
}

.result-section {
  margin: 0 2rem 2rem;
  padding: 1.5rem;
  background: linear-gradient(135deg, #e8f5e8, #f0f8f0);
  border-radius: 15px;
  border: 2px solid #4caf50;
}

.result-title {
  margin: 0 0 1rem 0;
  color: #2e7d32;
  font-size: 1.3rem;
  font-weight: 600;
}

.prompt-box {
  background: white;
  border-radius: 10px;
  padding: 1.5rem;
  position: relative;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.prompt-text {
  margin: 0;
  line-height: 1.6;
  font-size: 1.1rem;
  color: #333;
  padding-right: 100px;
  word-wrap: break-word;
}

.copy-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #2196f3, #1976d2);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap;
}

.copy-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(33, 150, 243, 0.3);
}

/* Responsive Design */
@media (max-width: 768px) {
  .fancy-prompt-generator {
    padding: 1rem;
  }
  
  .title {
    font-size: 2rem;
  }
  
  .subtitle {
    font-size: 1rem;
  }
  
  .input-section {
    padding: 1.5rem;
  }
  
  .button-section {
    padding: 0 1.5rem 1.5rem;
    flex-direction: column;
  }
  
  .generate-btn {
    min-width: unset;
  }
  
  .prompt-text {
    padding-right: 0;
    margin-bottom: 1rem;
  }
  
  .copy-btn {
    position: static;
    width: 100%;
    margin-top: 1rem;
  }
}

/* Animation for smooth transitions */
.fancy-prompt-generator * {
  transition: all 0.3s ease;
}

/* Hover effects for better interactivity */
.input:hover,
.select:hover {
  border-color: #bbb;
}

/* Focus states for accessibility */
.generate-btn:focus,
.clear-btn:focus,
.copy-btn:focus {
  outline: 3px solid rgba(102, 126, 234, 0.3);
  outline-offset: 2px;
}
</style>
