<template>
  <div class="home">
    <ToolBar/>
  </div>
</template>

<script>
import ToolBar from '@/components/ToolBar.vue'
export default {
  name: 'HomeView',
  components: {
    ToolBar
  }
}
</script>
<style>
.home{
  background-color: #FAB529;
}
</style>