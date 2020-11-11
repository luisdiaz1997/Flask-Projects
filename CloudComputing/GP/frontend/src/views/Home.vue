<template>
    <div id="home">
        <b-container>
            <Quotes :loading="quotesLoading" :quotes="quotes"/>
        </b-container>
    </div>
</template>
<script>
import axios from 'axios'
import Quotes from '@/components/Quotes.vue'
export default {
    name: "Home",
    components: {Quotes},
    data(){
        return{
            quotesLoading:true,
            quotes: null
        }
    },
    mounted(){
        axios.get('http://127.0.0.1:5000/get_quotes').then((response)=>{
            this.quotes= response.data
            this.quotesLoading=false
        })
    }

    
}
</script>

<style scoped>

</style>