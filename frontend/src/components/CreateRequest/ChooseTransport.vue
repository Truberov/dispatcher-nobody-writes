<template>
  <div>
    <v-row style="margin-top: 3%">
      <v-col>
        <h2>Выберете транспорт</h2>
      </v-col>
    </v-row>
    <v-row style="margin-top: 3%; margin-left: 2%; margin-right: 2%;   justify-content: center">
      <v-row style="align-items: flex-end; justify-content: space-around">
        <v-col class="item" cols="2" v-for="item in transport" :key="item" @click="select(item)">
          <div :class="{'selected' : selected && selected.type === item.type}">
            <v-img max-height="350" :src="item.img"></v-img>
            <h3>{{ item.name }}</h3>
          </div>
        </v-col>
      </v-row>
      <v-row style="margin-top: 3%">
        <v-col>
          <v-btn :disabled="!selected">
            Далее
          </v-btn>
        </v-col>
      </v-row>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "CreateRequest",

  data: () => ({
    transport: [
      {
        img: require('@/assets/aerialplatform.png'),
        name: 'Автовышка',
        type: 'aerialplatform'
      },
      {
        img: require('@/assets/loader.png'),
        name: 'Погрузчик',
        type: 'loader'
      },
      {
        img: require('@/assets/truckcrane.png'),
        name: 'Кран',
        type: 'truckcrane'
      }
    ],
    selected: null,
    isSelected: false
  }),
  methods: {
    select(item) {
      this.selected = item
    }
  }
}
</script>

<style scoped>
.item {
  cursor: pointer;
  transform: scale(1);
  transition: all 0.3s;
}

.item:hover {
  background: rgba(217, 217, 217, 0.5);
  border-radius: 10px;
  transition: all 0.3s;
  transform: scale(1.1);
}

.selected {
  border-radius: 10px;
  transform: scale(1.05);
  background: rgba(217, 217, 217, 0.5);
  transition: all 0.3s;
}
</style>