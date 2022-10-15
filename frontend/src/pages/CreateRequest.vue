<template>
  <div>
    <ToolBar/>
    <h1 class="mt-10">Создать заявку</h1>
    <ChooseTransport class="mt-10" v-if="!isChooseTransport" @choosed-transport="isChooseTransport = true"/>
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