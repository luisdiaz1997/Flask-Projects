<template>
  <div class="home">
    
    <b-container>
      <ImageUploader :image="image" @changed-image="updateImage"/>
      <AudioUploader/>
      <TextUploader/>
    </b-container>

    <b-button @click="get_audio"> Click me to get audio</b-button>
  </div>
</template>

<script>
// @ is an alias to /src
import ImageUploader from '@/components/ImageUploader.vue'
import AudioUploader from '@/components/AudioUploader.vue'
import TextUploader from '@/components/TextUploader.vue'

import axios from "axios"
export default {
  name: 'Home',
  components: {
    ImageUploader,
    AudioUploader,
    TextUploader
  },
  methods:
  {
    updateImage(newImage){
      this.image=newImage
      this.$store.commit('replaceImage', this.image)
    },
    get_audio()
    {
      let formData = new FormData();
      formData.append('text', 'Hello universe');
      let config=  { 
          headers: {
          'Content-Type': 'multipart/form-data'
          }
      }
      axios.post('http://127.0.0.1:5000/text_to_audio', formData, config).then((response)=>{
          console.log(response)
          
          })
    }
  },
  data(){
    return{
      image:null
    }
  },
  mounted(){
    this.image = this.$store.state.image
  }
}
</script>
