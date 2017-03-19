$(document).ready(function () {
    // validating signup form
    $(function () {
        $("form[name='login_form']").validate({
            rules: {
                email: {
                    required: true,
                    email: true,
                    remote: {
                        url: "/_check_email_login",
                        method: 'POST',
                        data: {
                            email: function () {
                                return $("#email").val();
                            }
                        }
                    }
                },
                password: {
                    required: true,
                    minlength: 5
                }
            },
            messages: {
                email: {
                    required: "Please provide email",
                    minlength: "Please provide a valid email",
                    remote: "The email provided is does not exists, Please signup <a href='/signup'>here</a>"
                },
                password: {
                    required: "Please provide a password",
                    minlength: "Your password must be at least 5 characters long"
                }
            },
            submitHandler: function (form) {
                form.submit();
            }
        });
    });
});