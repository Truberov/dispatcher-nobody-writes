<template>
  <div>
    <ToolBar/>
    <h1 style="margin-top: 3%">Создать заявку</h1>
    <ChooseTransport v-if="!isChooseTransport" @choosed-transport="isChooseTransport = true"/>
  </div>
</template>

<script>
import ToolBar from '@/components/ToolBar.vue'
import ChooseTransport from '@/components/CreateRequest/ChooseTransport.vue'

export default {
  name: 'CreateRequest',
  components: {
    ToolBar,
    ChooseTransport
  },
  data: () => ({
    isChooseTransport: false
  })
}
</script>
<style>

</style>