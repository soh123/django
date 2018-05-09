<script type="text/javascript">
function cart_del(cart_id){		
	var del = confirm('Are you sure?');
	if(del){
		$.get('/cart/delete'+cart_id+'/',function(data){
			if(data.ok==1){
				$('ul').remove('#'+cart_id);
			}
		});
	}
}

function total(){
	var total1=0;
	var total_count=0;
	$('.col07').each(function(){
		count = $(this).prev().find('input').val();
		price = $(this).prev().prev().text();
		total0 = parseFloat(count)*parseFloat(price);
		$(this).text(total0.toFixed(2)+'元');
		total1+=total0;
		total_count++;
	});
	$('#total').text(total1.toFixed(2));
	$('.total_count1').text(total_count);
}

$(function(){
	total();
	/*全选，全销*/
	$('#check_all').click(function(){
		state=$(this).prop('checked');
		$(':checkbox:not(#check_all)').prop('checked',state);
		total();
	});
	/*//选择*/
	$(':checkbox:not(#check_all)').click(function(){
		if($(this).prop('checked')){
			if($(':checked').length+1==$(':checkbox').length){
				$('#check_all').prop('checked',true);
			}
		}else{
			$('#check_all').prop('checked',false);
		}
		total();
	});

	/*//数量+1*/
	$('.add').click(function(){
		txt=$(this).next();
		txt.val(parseFloat(txt.val())+1).blur();
	})；
	/*//数量-1*/
	$('.minus').click(function(){
		txt=$(this).prev();
		txt.val(parseFloat(txt.val())-1).blur();
	})；
	/*//手动改数量*/
	$('.num_show').blur(function(){
		count = $(this).val();
		if(count<=0){
			$(this).val(1);
			$(this).focus();
			return;
		}
		cart_id=$(this).parents('.cart_list_td').attr('id');
		$.get('/cart/edit'+cart_id+'_'+count+"/",function(data){
			if(data.ok==0){
				total();
			}else{
				$(this).val(data.ok);
			}
		})
	});
});
</script>