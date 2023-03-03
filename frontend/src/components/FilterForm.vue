<template>
  <div class="p-3 m-0 border-0 bd-example">
    <h1>Поиск спортивных объектов</h1>
    <form @submit="onSubmit">
      <div class="mb-3">
        <label class="typo__label form-label">Субъект федерации</label>
        <VueMultiselect
          v-model="fedEntity"
          :options="fedEntityOptions"
          label="name"
          track-by="name"
          @close="loadDistricts"
        ></VueMultiselect>
      </div>
      <div class="mb-3">
        <label class="typo__label form-label">Муниципальный округ</label>
        <VueMultiselect
          v-model="district"
          :options="districtOptions"
          label="name"
          track-by="name"
          @close="loadLocalities"
        ></VueMultiselect>
      </div>
      <div class="mb-3">
        <label class="typo__label form-label">Населённый пункт</label>
        <VueMultiselect
          v-model="locality"
          :options="localityOptions"
          label="name"
          track-by="name"
        ></VueMultiselect>
      </div>
      <div class="mb-3">
        <label class="typo__label form-label">Вид спорта</label>
        <VueMultiselect
          v-model="sportType"
          :options="sportTypeOptions"
          label="name"
          track-by="name"
        ></VueMultiselect>
      </div>
      <div class="mb-3">
        <label class="typo__label form-label">Тип спортивного объекта</label>
        <VueMultiselect
          v-model="sportObjectType"
          :options="sportObjectTypeOptions"
          label="name"
          track-by="name"
        ></VueMultiselect>
      </div>
      <button type="submit" class="btn btn-primary">Поиск</button>
    </form>
  </div>
</template>

<script lang="ts">
import VueMultiselect from 'vue-multiselect'
import { defineComponent } from 'vue'
import axios from 'axios'
import type { Choice } from '@/types'

export default defineComponent({
  name: 'FilterForm',
  components: {
    VueMultiselect
  },
  expose: ['fedEntity', 'district', 'locality', 'sportType', 'sportObjectType'],
  data(): {
    fedEntity: Choice
    fedEntityOptions: Choice[]
    district: Choice
    districtOptions: Choice[]
    locality: Choice
    localityOptions: Choice[]
    sportType: Choice
    sportTypeOptions: Choice[]
    sportObjectType: Choice
    sportObjectTypeOptions: Choice[]
  } {
    return {
      fedEntity: { id: undefined, name: 'Выберите субъект' },
      fedEntityOptions: [],
      district: { id: undefined, name: 'Выберите МО' },
      districtOptions: [],
      locality: { id: undefined, name: 'Выберите населённый пункт' },
      localityOptions: [],
      sportType: { id: undefined, name: 'Выберите вид спорта' },
      sportTypeOptions: [],
      sportObjectType: { id: undefined, name: 'Выберите тип спортивного объекта' },
      sportObjectTypeOptions: []
    }
  },
  methods: {
    loadFedEntities() {
      axios.get(`${import.meta.env.VITE_API_ENDPOINT}/federation-entities/`).then((response) => {
        this.fedEntityOptions = response.data
      })
    },
    loadDistricts() {
      axios
        .get(
          `${import.meta.env.VITE_API_ENDPOINT}/districts/${
            this.fedEntity ? `?fed_entity_id=${this.fedEntity.id}` : ''
          }`
        )
        .then((response) => {
          this.districtOptions = response.data
        })
    },
    loadLocalities() {
      axios
        .get(
          `${import.meta.env.VITE_API_ENDPOINT}/localities/${
            this.district ? `?district_id=${this.district.id}` : ''
          }`
        )
        .then((response) => {
          this.localityOptions = response.data
        })
    },
    loadSportTypes() {
      axios.get(`${import.meta.env.VITE_API_ENDPOINT}/sport-types/`).then((response) => {
        this.sportTypeOptions = response.data
      })
    },
    loadSportObjectTypes() {
      axios.get(`${import.meta.env.VITE_API_ENDPOINT}/sport-object-types/`).then((response) => {
        this.sportObjectTypeOptions = response.data
      })
    }
  },
  mounted() {
    this.loadFedEntities()
    this.loadSportTypes()
    this.loadSportObjectTypes()
  },
  props: {
    onSubmit: Function
  }
})
</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>
<style scoped></style>
