<template>
    <div id="image-uploader">
            <h2>Analyze Image</h2>
            <b-row>
                
                <b-col>
                    <img v-if="image" alt="Uploaded image" class="img-style" :src="getImPreview()">
                    <img v-else alt="Vue logo" class="imgStyle" src="../assets/logo.png">
                    <div v-if="imgDescription">
                        <p>{{imgDescription}}</p>
                    </div>
                </b-col>

                <b-col class="vcenter-content">
                    
                    <br>
                    <br>
                    <b-form-file
                    v-model="localImage"
                    :state="Boolean(image)"
                    placeholder="Choose a file or drop it here..."
                    drop-placeholder="Drop file here..."
                    ></b-form-file>
                    <div class="mt-3">Selected file: {{ image ? image.name : '' }}</div>
                    <br>
                    <b-button v-if="image" size="md"  class="mb-1" variant="primary" @click="analyzeImg">Analyze</b-button>
                </b-col>
            </b-row>
            <br>
            


        
    </div>
</template>


<script>
import axios from "axios";

export default {
  name: 'ImageUploader',
  props: {
    image: File
  },
  data(){
    return{
        localImage: null,

        imgDescription:null
    }
  },
  methods:
  {
        getImPreview()
        {
            return URL.createObjectURL(this.image);
        },
        analyzeImg(){
            let formData = new FormData();
            formData.append('image', this.image);
            let config=  { 
                headers: {
                'Content-Type': 'multipart/form-data'
                }
            }
            axios.post('http://127.0.0.1:5000/analyze_image', formData, config).then((response)=>{
                this.imgDescription = response.data["message"]

                })
        }
  },
  watch:
  {
      localImage(newImage)
      {
          this.imgDescription=null
          this.$emit('changed-image', newImage)
      }
  }


}
</script>


<style scoped>
.img-style{
    object-fit: contain;
    object-position: center;
    height: 400px;
    width: 100%;
}

.vcenter-content{
   margin-top:auto;
   margin-bottom:auto;
   /* display:block; */
}

</style>