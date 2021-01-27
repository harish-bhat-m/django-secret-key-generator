function copy_to_clipboard(){
	var input_obj_key = document.getElementById('id_secret_key');
	input_obj_key.select();
    input_obj_key.setSelectionRange(0, input_obj_key.value.length);
    document.execCommand("copy");
    alert("Copied the text: " + input_obj_key.value);
}