<template>
  <div>
    <ToolBar/>
    <h1 style="margin-top: 3%">Создать заявку</h1>
    <ChooseTransport v-if="!isChooseTransport" @choosed-transport="isChooseTransport = true"/>
    <ChooseDate  v-if="isChooseTransport" />
  </div>
</template>

<script>
import ToolBar from '@/components/ToolBar.vue'
import ChooseTransport from '@/components/CreateRequest/ChooseTransport.vue'
import ChooseDate from "@/components/CreateRequest/ChooseDate"
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

</style>