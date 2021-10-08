<template>
  <header>
    <Header />
  </header>
</template>

<script>
import Header from './components/header/Header.vue'

export default {
  name: 'App',
  components: {
    Header
  }
}
</script>

<style>
html{
  margin:0;
  padding:0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
