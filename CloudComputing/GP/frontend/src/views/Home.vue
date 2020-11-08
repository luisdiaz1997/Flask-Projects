<template>
  <div class="home">
    
    <DataUploader></DataUploader>
  </div>
</template>

<script>
// @ is an alias to /src
import DataUploader from '@/components/DataUploader.vue'

export default {
  name: 'Home',
  components: {
    DataUploader
  }
}
</script>
