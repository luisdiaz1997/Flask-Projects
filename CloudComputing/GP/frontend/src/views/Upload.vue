<template>
  <div class="upload">
    
    <b-container>
      <ImageUploader :image="image" @changed-image="updateImage"/>
      <AudioUploader/>
      <TextUploader/>
    </b-container>

  </div>
</template>

<script>
// @ is an alias to /src
import ImageUploader from '@/components/ImageUploader.vue'
import AudioUploader from '@/components/AudioUploader.vue'
import TextUploader from '@/components/TextUploader.vue'


export default {
  name: 'Upload',
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
