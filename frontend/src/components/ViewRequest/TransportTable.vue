<template>
  <div>
    <v-row style="justify-content: center">
      <v-col cols="10">
        <v-data-table
            style="border: solid lightgray 1px"
            locale="ru"
            :headers="headers"
            :items="transport"
        >
        </v-data-table>
      </v-col>
    </v-row>
  </div>
</template>

<script>

export default {
  name: "TransportTable",
  data: () => ({
    transport: [
      {
        id: 16,
        type: "Парк автовышек",
        characteristic: "Автовышка (35 м)",
        name: "КАМАЗ 43114",
        plate_number: "А110АА/999",
        status: "FREE",
        is_active: false,
        performer: null
      },
      {
        id: 18,
        type: "Парк автовышек",
        characteristic: "Автовышка (35 м)",
        name: "КАМАЗ 43114",
        plate_number: "А112АА/999",
        status: "FREE",
        is_active: false,
        performer: null
      },
      {
        id: 19,
        type: "Парк автовышек",
        characteristic: "Автовышка (35 м)",
        name: "КАМАЗ 43114",
        plate_number: "А113АА/999",
        status: "FREE",
        is_active: false,
        performer: null
      }
    ],
    headers: [{
      text: 'Тип транспорта',
      value: 'type'
    },
      {
        text: 'Характеристика',
        value: 'characteristic'
      },
      {
        text: 'Наименование',
        value: 'name'
      },
      {
        text: 'Статус',
        value: 'status'
      }
    ]
  })
}
</script>

<style scoped>

</style>