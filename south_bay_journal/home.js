function filterPosts(filter_name){
    posts_elements = document.getElementsByClassName('post');
    show_all = false;
    if (filter_name == 'all'){
        show_all = true;
    }
    for (var i = 0 ; i < posts_elements.length ; i++){
        var class_name = posts_elements[i].className;
        if (show_all){
            posts_elements[i].hidden = false;
            continue;
        }
        if (!class_name.includes(filter_name)){
            posts_elements[i].hidden = true;
        } else {
            posts_elements[i].hidden = false;
        }
    }
}

function handleContact(){
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    const body = `From: ${email} \n Message: ${message}`;
    const subject = "South Bay Journal message";
    const myEmail = 'dhavaljjani01@gmail.com'
    const mailto = `mailto:${myEmail}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    window.open(mailto);
}