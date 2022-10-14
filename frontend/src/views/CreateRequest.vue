<template>
  <div class="home">
    <ToolBar/>
    <ChooseTransport v-if="!isChooseTransport" @choosed-transport="isChooseTransport = true"/>
    <ChooseDate v-if="isChooseTransport" />
  </div>
</template>

<script>
import ToolBar from '@/components/ToolBar.vue'
import ChooseTransport from '@/components/ChooseTransport.vue'
import ChooseDate from '@/components/ChooseDate'
export default {
  name: 'CreateRequest',
  components: {
    ToolBar,
    ChooseTransport,
    ChooseDate
  },
  data: () => ({
    isChooseTransport: false
  })
}
</script>
<style>
.home{
  height: 100vh;
}
</style>