/** @odoo-module **/

import {Component,mount,whenReady,onWillStart,useState} from '@odoo/owl'
import {templates} from '@web/core/assets'
import {jsonrpc} from '@web/core/network/rpc_service'

class ToyCommerce extends Component{
    setup(){
        this.regionData = useState([])
        this.stateData = useState([])
        onWillStart(async () => {
            try {
                const data = await jsonrpc('/toy_commerce/get_regions',{});
                console.log(data)
                this.regionData.splice(0, this.regionData.length, ...data);
            } catch (error) {
                console.error('Error fetching regions:', error);
            }
        });
    }

    async onChangeData(event) {
        const selectedRegionId = parseInt(event.target.value);
        console.log("id -----",selectedRegionId)
        while (this.stateData.length > 0) {
            this.stateData.pop();
          }
        try {
            const states = await jsonrpc('/toy_commerce/get_state_price', {region_id:selectedRegionId});
            states.forEach((items) => this.stateData.push(items))
            // this.stateData.splice(0, this.stateData.length, ...states);
        } catch (error) {
            console.error('Error fetching states:', error);
        }
      
    }
    setDelPrice(e){
        const id = e.target.value;
        const data = this.stateData.find((element) => element.id === parseInt(id))
        $('#deli_price').val(parseInt(data.price))
        var monetary_field_total = $('#monetary_field_total').val()
        let sum_totl = parseInt(monetary_field_total) + parseInt(data.price)
        $('.final_total').html(sum_totl)
    }

    callFast(e){
       const res = e.target.value;
       if(res === 'normal'){
         $('.fast_layer').addClass('d-none')
       }else{
        $('.fast_layer').removeClass('d-none')
       }
    }
   
}
ToyCommerce.template='toy_commerce.Template'
whenReady(()=>{
    const element = document.querySelector('#reg_and_state')
    if(element){
        mount(ToyCommerce,element,{templates})
    }
})
