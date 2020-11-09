<template>
    <div id="DataUploader">
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
            <h2>Analyze Audio</h2>

            <br>
            <b-row>
                <b-col >
                    <h3>Hold to record</h3>
                    <vue-record-audio @result="onResult"/>
                </b-col>
                <b-col>
                    <h3>Audio Files</h3>
                    <div v-if="recordings.length" class="recorded-audio">
                        <div v-for="(record, index) in recordings" :key="index" class="recorded-item">
                            <b-button-group>
                            <audio :src="record.src" controls></audio>

                            <b-button size="md"  class="mb-1" variant="dark" pill @click="removeRecord(index)">
                                <b-icon icon="trash-fill" aria-hidden="true"></b-icon>
                            </b-button>
                            <b-button size="sm"  variant="primary" pill @click="analyzeAudio(index)">Analyze</b-button>
                            </b-button-group>
                            <br>    
                            <div v-if="record.description">
                                <p class="text-light">{{record.description}}</p>
                            </div>
                        </div>
                    </div>
                    <div v-else class="recorded-audio">
                        <p class="text-light">No audio available</p>
                    </div>
                </b-col>
            </b-row>


        
    </div>
</template>


<script>
import axios from "axios";

export default {
  name: 'DataUploader',
  props: {
    image: File
  },
  data(){
    return{
        localImage: null,
        recordings:[],
        imgDescription:null,
        currStream:null
    }
  },
  methods:
  {
        getImPreview()
        {
            return URL.createObjectURL(this.image);
        }
        ,
        onResult (data) {
            let data_blob  = new Blob([data], { 'type': 'audio/webm' })
            this.recordings.push({
                src: URL.createObjectURL(data_blob),
                data: data_blob,
                description: null
            })
        },
        removeRecord (index) {
            this.recordings.splice(index, 1)
        },
        analyzeAudio(index)
        {
            let formData = new FormData();
            formData.append('file', this.recordings[index].data);
            let config=  { 
                headers: {
                'Content-Type': 'multipart/form-data'
                }
            }
            axios.post('http://127.0.0.1:5000/analyze_audio', formData, config).then((response)=>{
                this.recordings[index].description = response.data["message"]

                })
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
.recorded-audio{
    border:1px solid black;
    padding: 10px 10px;
    background: grey;
    border-radius: 20px;
}
</style>