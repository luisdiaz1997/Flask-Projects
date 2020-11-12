<template>
    <div id="home">
        <b-container>
            <Quotes :loading="quotesLoading" :quotes="quotes"/>
        </b-container>
    </div>
</template>
<script>
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
        this.$api.get('/get_quotes').then((response)=>{
            console.log(response.data)
            this.quotes= response.data
            this.quotesLoading=false
        })
    }

    
}
</script>

<style scoped>

</style>