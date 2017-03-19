$(document).ready(function () {
    // validating signup form
    $(function () {
        $("form[name='signup_form']").validate({
            rules: {
                email: {
                    required: true,
                    email: true,
                    remote: {
                        url: "/_check_email_signup",
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
                },
                r_password: {
                    required: true,
                    minlength: 5,
                    equalTo: "#password"
                }
            },
            messages: {
                email: {
                    required: "Please provide email",
                    minlength: "Please provide a valid email",
                    remote: "Email already signed up! Please login <a href='/login'> here </a>"
                },
                password: {
                    required: "Please provide a password",
                    minlength: "Your password must be at least 5 characters long"
                },
                r_password: {
                    required: "Please provide a password",
                    minlength: "Your password must be at least 5 characters long",
                    equalTo: "Passwords provided do not match!"
                }
            },
            submitHandler: function (form) {
                form.submit();
            }
        });
    });
});