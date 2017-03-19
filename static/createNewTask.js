$(document).ready(function () {
    $("#newTask").click(function () {
        var newTaskTitleValue = $("#newTaskTitle").val().trim();
        var newTaskDescriptionValue = $("#newTaskDescription").val().trim();
        var reloadRequired = true;
        if (!newTaskTitleValue) {
            $("#newTaskTitleError").text("cannot be blank or empty!")
            reloadRequired = false;
        } else if (newTaskTitleValue) {
            $("#newTaskTitleError").text("");
            reloadRequired = false;
        }
        if (!newTaskDescriptionValue) {
            $("#newTaskDescriptionError").text("cannot be blank or empty!")
        } else if (newTaskDescriptionValue) {
            $("#newTaskDescriptionError").text("")
        }
        if (newTaskTitleValue && newTaskDescriptionValue) {
            $.ajax({
                type: "POST",
                url: '/create_new_task',
                data: {
                    new_task_title_value: newTaskTitleValue,
                    new_task_desription_value: newTaskDescriptionValue
                },
                success: function () {
                    $("#newTaskError").text("Task is successfully created!");
                },
                failure: function () {
                    $("#newTaskError").html("Something went wrong :( <br> Please try again!!!");
                }
            });
        }
        $('#newTaskTitle').val('');
        $('#newTaskDescription').val('');
        if (reloadRequired){
            location.reload();
        }
    });
});