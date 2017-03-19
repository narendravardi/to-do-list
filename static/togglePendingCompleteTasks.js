$(document).ready(function () {
    $("button").click(function () {
        var idOfbutton = $(this).attr('id');
        if (idOfbutton.includes("mark_as_complete_id")) {
            var taskID = parseInt(this.id.match(/\d+$/)[0].trim(), 10);
            $.ajax({
                type: "POST",
                url: '/mark_task_complete',
                data: {
                    task_id_toggle: taskID
                }
            });
            console.log(taskID);
        }
        else if (idOfbutton.includes("mark_as_pending_id")) {
            var taskID = parseInt(this.id.match(/\d+$/)[0].trim(), 10);
            $.ajax({
                type: "POST",
                url: '/mark_task_pending',
                data: {
                    task_id_toggle: taskID
                }
            });
            console.log(taskID);
        }
        location.reload();
    });
});