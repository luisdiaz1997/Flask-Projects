<template>
<div id="numbers">
    <b-row>
        <b-col sm="12" lg="6" md="6">
            <div id="drawNumber">
                <canvas id="mnist" ref="mnist" @mousedown="startPainting" @mousemove="sketch" 
                @mouseup="stopPainting" @mouseleave="stopPainting"
                v-hammer:panstart="startPainting"  v-hammer:panmove="sketch" v-hammer:panend="stopPainting"/>
            </div>
             <b-button variant="info" @click="clearPainting">Clear</b-button>
        </b-col>
        <b-col sm="12" lg="6" md="6">
            <Barchart :labels="labels" :predictions="predictions"/>
        </b-col>
    </b-row>
</div>   
</template>

<script>
import Barchart from "@/components/Barchart.vue";
export default {
    name:"Numbers",
    components: {
        Barchart
    },
    data(){
        return {
            ctx: null,
            paint:false,
            strideSize:12,
            leftOff: 0,
            topOff:0,
            height:0,
            width: 0,
            color: "black",
            mouse_pos:{x: innerWidth/2, y:innerHeight/2},
            labels : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            predictions:[0, 0, 0, 0, 0, 0,0,0,0,0]
        }
    },
    destroyed(){
        window.removeEventListener('resize', this.onResize)
    },
    mounted(){
        this.initialize()
        window.addEventListener('resize', this.onResize)
    },
    methods:{
        initialize(){
            let mnist = this.$refs.mnist
            mnist.height = mnist.clientHeight
            mnist.width = mnist.clientWidth
            this.height = mnist.height
            this.width = mnist.width
            this.setOffsets(mnist)
            this.ctx = mnist.getContext("2d")
        },
        setOffsets(mnist){
            this.leftOff = mnist.getBoundingClientRect().x
            this.topOff = mnist.getBoundingClientRect().y
        },
        onResize() {
            this.initialize()
        },
        startPainting(e){
            this.paint= true
            this.getPosition(e)
        },
        getPosition(e){
            this.mouse_pos.x = e.clientX - this.leftOff
            this.mouse_pos.y = e.clientY  - this.topOff
        },
        stopPainting(){
            if (!this.paint){
                return;
            }
            this.paint = false
            let formData = new FormData()
            // let imgData = this.ctx.getImageData(0, 0, this.width, this.height ).data
            formData.append('image', this.$refs.mnist.toDataURL("image/png"))
            let config=  { 
                headers: {
                'Content-Type': 'multipart/form-data'
                }
            }
            this.$api.post('/process_number', formData, config).then((response)=>{
                this.predictions = response.data.predictions
            })
        },
        clearPainting(){
            this.ctx.clearRect(0, 0, this.width, this.height)
        },
        sketch(e){
            if (!this.paint) return;
            this.ctx.beginPath()
        
            this.ctx.lineWidth = this.strideSize;
            this.ctx.lineCap = 'butt';
            this.ctx.strokeStyle = this.color;
        
            this.ctx.moveTo(this.mouse_pos.x, this.mouse_pos.y)
        
            this.getPosition(e)
        
            this.ctx.lineTo(this.mouse_pos.x , this.mouse_pos.y)
            this.ctx.closePath()
            this.ctx.stroke()
        }
    }

    
}
</script>

<style scoped>
#drawNumber{
    height: 25vw;
    width: auto;
    min-height: 300px;
    background: black;
    padding: 5%
}
#mnist{
    background: white;
    height: 100%;
    width: 100%;
}

</style>