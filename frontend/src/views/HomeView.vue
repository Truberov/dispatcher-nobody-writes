<template>
  <div class="home">
    <ToolBar/>
    <CreateRequest/>
  </div>
</template>

<script>
import ToolBar from '@/components/ToolBar.vue'
import CreateRequest from '@/components/CreateRequest.vue'
export default {
  name: 'HomeView',
  components: {
    ToolBar,
    CreateRequest
  }
}
</script>
<style>
.home{
  background-color: #FAB529;
}
</style>