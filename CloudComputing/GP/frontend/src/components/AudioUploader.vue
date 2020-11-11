<template>
    <div id="audio-uploader">
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

export default {
    name:'AudioUploader',
    data(){
        return{
            recordings:[],
        }
    },
    methods:{
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
            this.$api.post('/analyze_audio', formData, config).then((response)=>{
                this.recordings[index].description = response.data["message"]

                })
        },
    }
    
}
</script>

<style scoped>

.recorded-audio{
    border:1px solid black;
    padding: 10px 10px;
    background: grey;
    border-radius: 20px;
}

</style>