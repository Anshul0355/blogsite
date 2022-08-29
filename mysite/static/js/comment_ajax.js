// $(document).ready(function(){
//  debugger  
//   $('.comment-form').click(function(event){
//     debugger
//     // const url = "/home/detail/"+id+"/";
//     post_id=pk;
//     $.ajax({
//       type: 'POST',
//       url:  'http:8000/home/detail/id/',
//       dataType: 'json',
//       beforeSend: function() {
//         $("#myModal").modal("show");
//       }, 
//       success: function(response) {
//         debugger
//         console.log("Success!",response);
//         $("#myModal .modal-content").html(response['context']);
//       }
//     });
//   });

// });

// $(document).ready(function() {
//     $("#submit-comment").click(function(event) {
//         debugger
//         // event.preventDefault();
//         var id = $(this).attr("value");
//         var url = "/home/detail/"+id+"/";
//         var dataPosted = $("#mainSubmit").serialize();

//         $.ajax({
//             type: 'POST',
//             url: url,
//             data: dataPosted,

//             success: function(data) {
//                 debugger
//                 alert("Success!");
//                 $(".modal-body").html(data);

//             },
//             error: function (textStatus, errorThrown) {
//                 alert('Errors!');
//             }
//         });
//     });
// });








// $('#commenting').text(response['content']);


// $("#myModal.modal-content").html(response['context']);