<template>
  <div>
      <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'App',
    provide () {
      return {
        reload: this.reload
      }
    }
  }
</script>