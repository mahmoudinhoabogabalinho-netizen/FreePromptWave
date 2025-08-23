<template>
  <div id="app">
    <header class="app-header">
      <h1>FreePromptWave</h1>
      <p>موجة البرومبت المجانية - Free AI Prompt Sharing Platform</p>
    </header>
    
    <main class="main-content">
      <PromptList />
    </main>
    
    <footer class="app-footer">
      <p>&copy; 2025 FreePromptWave - Open Source AI Prompt Platform</p>
    </footer>
  </div>
</template>

<script>
import PromptList from './components/PromptList.vue'

export default {
  name: 'App',
  components: {
    PromptList
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
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
  padding: 2rem;
  min-height: calc(100vh - 200px);
}

.app-footer {
  background-color: #f8f9fa;
  text-align: center;
  padding: 1rem;
  border-top: 1px solid #e0e0e0;
}
</style>
