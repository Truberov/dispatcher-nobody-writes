<template>
  <div class="home">
    <ToolBar/>
    <h1 class="mt-10">Создать заявку</h1>
    <ChooseTransport v-if="!isChooseTransport" @choosed-transport="isChooseTransport = true"/>
    <ChooseDate v-if="isChooseTransport"/>
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
  background-color: #FAB529;
}

</style>