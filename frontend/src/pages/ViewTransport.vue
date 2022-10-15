<template>
  <div>
    <ToolBar/>
    <h1 style="margin-top: 3%">Просмотр транспорта</h1>
    <TransportTable/>
  </div>
</template>

<script>
import ToolBar from '@/components/ToolBar.vue'
import TransportTable from '@/components/ViewRequest/TransportTable'

export default {
  name: "ViewTransport",
  components: {
    ToolBar,
    TransportTable
  }
}
</script>

<style scoped>

</style>