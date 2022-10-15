<template>
  <div>
    <v-row style="justify-content: center; ">
      <v-col cols="10">
        <v-data-table
            style="border: solid lightgray 1px"
            class="elevation-1"
            :server-items-length="totalItems"
            :headers="headers"
            :items="transport"
            :footer-props="footerProps"
            :page.sync="paginatorOptions.page"
            :options.sync="paginatorOptions"
            :loading="loading"
            loading-text="Загрузка..."
            @pagination="changePage"
        >
          <template v-slot:[`item.status`]="{ item }">
            <p v-if="item.status === 'FREE'">Свободен</p>
            <p v-else>
              Занят
            </p>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "TransportTable",
  data: () => ({
    url: 'http://127.0.0.1:8000/api/transport/',
    transport: [],
    headers: [
      {
        text: 'Тип транспорта',
        value: 'type',
        width: '15%'
      },
      {
        text: 'Характеристика',
        value: 'characteristic',
        width: '20%'
      },
      {
        text: 'Наименование',
        value: 'name',
        width: '25%'
      },
      {
        text: 'Статус',
        value: 'status',
        width: '10%'
      }
    ],
    paginatorOptions: {
      page: 1,
      itemsPerPage: 15
    },
    loading: false,
    totalItems: 0,
    footerProps: {
      'items-per-page-options': [15],
      itemsPerPageText: '',
      pageText: '',
      'show-current-page': true
    }
  }),
  mounted() {
    this.getTransport()
  },
  methods: {
    changePage() {
      this.getTransport()
    },
    async getTransport() {
      this.loading = true
      const res = await axios.get(this.url, {
        params: {
          page: this.paginatorOptions.page,
          per_page: 15
        }
      })
      this.transport = res.data.results
      this.totalItems = res.data.count
      this.loading = false
    }
  }
}
</script>

<style scoped>

</style>