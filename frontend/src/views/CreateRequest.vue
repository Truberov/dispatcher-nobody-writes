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
<style lang="scss">
.home {
  height: 100vh;
}


.fade2-enter-active, .fade2-leave-active {
  transition: all .6s;
}

.fade2-enter, .fade2-leave-to /* .fade-leave-active до версии 2.1.8 */
{
  position: absolute;
  opacity: 0;
  transform: translateY(200px);
}

</style>