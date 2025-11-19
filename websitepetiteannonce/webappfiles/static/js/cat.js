$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();

    var checkbox = $('table tbody input[type="checkbox"]');
    $("#selectAll").click(function(){
        if(this.checked){
            checkbox.each(function(){
                this.checked = true;                        
            });
        } else{
            checkbox.each(function(){
                this.checked = false;                        
            });
        } 
    });
    checkbox.click(function(){
        if(!this.checked){
            $("#selectAll").prop("checked", false);
        }
    });

	$('.edit').click(function () {
		var category_id = $(this).data('category-id');
		var category_type = $(this).closest('tr').find('td:nth-child(2)').text();
	
		$('#edit_category_id').val(category_id);
		$('#edit_category_type').val(category_type);
	
		$(this).html('<i class="fas fa-edit"></i> Edit');
	});

    $('.delete').click(function () {
        var category_id = $(this).data('category-id');
        $('#delete_category_id').val(category_id);
    });
    
    
    




	
	
});