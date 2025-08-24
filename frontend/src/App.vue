<template>
  <div id="app">
    <!-- Privacy Policy Notice Banner -->
    <div class="privacy-notice">
      <div class="privacy-content">
        <div class="privacy-icon">🔒</div>
        <div class="privacy-text">
          <div class="privacy-title">
            <strong>Zero Data • Zero Logging • No Liability</strong>
          </div>
          <div class="privacy-subtitle">
            لا نحفظ أي بيانات | We don't store any data | Tous local, aucun serveur externe
          </div>
        </div>
      </div>
    </div>
    
    <header class="app-header">
      <h1>FreePromptWave</h1>
      <p>موجة البرومبت المجانية - Free AI Prompt Sharing Platform</p>
    </header>
    
    <main class="main-content">
      <FancyPromptGenerator />
    </main>
    
    <footer class="app-footer">
      <p>© 2025 FreePromptWave - Open Source AI Prompt Platform</p>
      <p class="footer-privacy">
        ⚠️ لا يوجد ربط قانوني أو تقني بين هذه المنصة وأي هوية زائر | No legal or technical connection to any visitor identity
      </p>
    </footer>
  </div>
</template>

<script>
import FancyPromptGenerator from './components/FancyPromptGenerator.vue'

export default {
  name: 'App',
  components: {
    FancyPromptGenerator
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

/* Privacy Notice Banner */
.privacy-notice {
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
  color: white;
  padding: 8px 0;
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.privacy-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 20px;
  gap: 15px;
}

.privacy-icon {
  font-size: 1.5em;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.privacy-text {
  text-align: center;
}

.privacy-title {
  font-size: 0.95em;
  font-weight: bold;
  margin-bottom: 2px;
}

.privacy-subtitle {
  font-size: 0.8em;
  opacity: 0.9;
}

.app-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-align: center;
  padding: 2rem;
}

.app-header h1 {
  margin: 0;
  font-size: 2.5em;
}

.app-header p {
  margin: 0.5rem 0 0 0;
  font-size: 1.2em;
  opacity: 0.9;
}

.main-content {
  padding: 0;
  min-height: calc(100vh - 280px);
}

.app-footer {
  background-color: #f8f9fa;
  text-align: center;
  padding: 1rem;
  border-top: 1px solid #e0e0e0;
}

.footer-privacy {
  font-size: 0.8em;
  color: #666;
  margin-top: 0.5rem;
  font-style: italic;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .privacy-content {
    flex-direction: column;
    gap: 8px;
    padding: 0 15px;
  }
  
  .privacy-title {
    font-size: 0.85em;
  }
  
  .privacy-subtitle {
    font-size: 0.75em;
  }
  
  .app-header h1 {
    font-size: 2em;
  }
  
  .app-header p {
    font-size: 1em;
  }
}
</style>
