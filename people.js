function get_and_save_book(){ 
    // Hide any existing warning messages
    $('#titleWarning').hide();
    $('#authorWarning').hide();
    $('#summaryWarning').hide();
    $('#scoreWarning').hide();
    $('#imageWarning').hide();
    $('#genresWarning').hide();
    $('#seriesWarning').hide();

    let title = $.trim( $("#title").val());
    let author = $.trim( $("#author").val());
    let summary = $.trim( $("#summary").val());
    let score = $.trim( $("#score").val());
    let image = $.trim( $("#image").val());
    let genres = $.trim( $("#genres").val());
    let series = $.trim( $("#series").val());

    // Check if the title field is empty
    if (!title) { // If the title field is empty
        // Display a warning message
        $('#titleWarning').text('Enter Title').show(); //
        // Set the focus to the title field
        $("#title").focus();
    }

    // Check if the author field is empty
    else if (!author) { // If the author field is empty
        // Display a warning message
        $('#authorWarning').text('Enter Author').show(); //
        // Set the focus to the author field
        $("#author").focus();
    }

    // Check if the summary field is empty
    else if (!summary) { // If the summary field is empty
        // Display a warning message
        $('#summaryWarning').text('Enter Summary').show(); //
        // Set the focus to the summary field
        $("#summary").focus();
    }

    // Check if the score field is empty
    else if (!score) { // If the score field is empty
        // Display a warning message
        $('#scoreWarning').text('Enter Rating').show(); //
        // Set the focus to the score field
        $("#score").focus();
    }
    // Check if the score field is empty or not a number
    else if (isNaN(score)) { // If score is not a number
        // Display a warning message
        $('#scoreWarning').text('Enter a Valid Rating').show(); //
        // Set the focus to the score field
        $("#score").focus();
    }

    // Check if the image field is empty
    else if (!image) { // If the image field is empty
        // Display a warning message
        $('#imageWarning').text('Enter Image').show(); //
        // Set the focus to the image field
        $("#image").focus();
    }

    // Check if the genres field is empty
    else if (!genres) { // If the genres field is empty
        // Display a warning message
        $('#genresWarning').text('Enter Genres').show(); //
        // Set the focus to the genres field
        $("#genres").focus();
    }

    // Check if the series field is empty
    else if (!series) { // If the series field is empty
        // Display a warning message
        $('#seriesWarning').text('Enter Series').show(); //
        // Set the focus to the series field
        $("#series").focus();
    }

    else { // If all the fields are filled
        let data_to_save = {"title": title, "author": author, "summary": summary, "score": score, "image": image, "genres": genres, "series": series}         
        
        $.ajax({
            type: "POST",
            url: "add_items",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),

            success: function(result){
                // returns all of the array
                // displayNames(data)

                console.log(result);
                let id = result["new_id"];
                console.log(id);
                $("#title").val("") // clears the textarea
                $("#author").val("") // clears the textarea
                $("#summary").val("") // clears the textarea
                $("#score").val("") // clears the textarea
                $("#image").val("") // clears the textarea
                $("#genres").val("") // clears the textarea
                $("#series").val("") // clears the textarea

                // Display success message
                $("#successMessage").text("New item successfully created.");
                
                // Add link to view item
                let viewItemLink = `<a href="/view/${id}">View Item</a>`;
                $("#viewItemLink").html(viewItemLink);
                $("#title").focus();

            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    }
}


function edit_book(id){
    // Hide any existing warning messages
    console.log(id);
    $('#titleWarning').hide();
    $('#authorWarning').hide();
    $('#summaryWarning').hide();
    $('#scoreWarning').hide();
    $('#imageWarning').hide();
    $('#genresWarning').hide();
    $('#seriesWarning').hide();

    let title = $.trim( $("#title").val());
    let author = $.trim( $("#author").val());
    let summary = $.trim( $("#summary").val());
    let score = $.trim( $("#score").val());
    let image = $.trim( $("#image").val());
    let genres = $.trim( $("#genres").val());
    let series = $.trim( $("#series2").val());

    // Check if the title field is empty
    if (!title) { // If the title field is empty
        // Display a warning message
        $('#titleWarning').text('Enter Title').show(); //
        // Set the focus to the title field
        $("#title").focus();
    }

    // Check if the author field is empty
    else if (!author) { // If the author field is empty
        // Display a warning message
        $('#authorWarning').text('Enter Author').show(); //
        // Set the focus to the author field
        $("#author").focus();
    }

    // Check if the summary field is empty
    else if (!summary) { // If the summary field is empty
        // Display a warning message
        $('#summaryWarning').text('Enter Summary').show(); //
        // Set the focus to the summary field
        $("#summary").focus();
    }

    // Check if the score field is empty
    else if (!score) { // If the score field is empty
        // Display a warning message
        $('#scoreWarning').text('Enter Rating').show(); //
        // Set the focus to the score field
        $("#score").focus();
    }

    else if (isNaN(score)) { // If score is not a number
        // Display a warning message
        $('#scoreWarning').text('Enter a Valid Rating').show(); //
        // Set the focus to the score field
        $("#score").focus();
    }

    // Check if the image field is empty
    else if (!image) { // If the image field is empty
        // Display a warning message
        $('#imageWarning').text('Enter Image').show(); //
        // Set the focus to the image field
        $("#image").focus();
    }

    // Check if the genres field is empty
    else if (!genres) { // If the genres field is empty
        // Display a warning message
        $('#genresWarning').text('Enter Genres').show(); //
        // Set the focus to the genres field
        $("#genres").focus();
    }

    // Check if the series field is empty
    else if (!series) { // If the series field is empty
        // Display a warning message
        $('#seriesWarning').text('Enter Series').show(); //
        // Set the focus to the series field
        $("#series").focus();
    }

    else { // If all the fields are filled
        
        let data_to_save = {"id": id, "title": title, "author": author, "summary": summary, "score": score, "image": image, "genres": genres, "series": series}         
        console.log(data_to_save);

        $.ajax({
            type: "POST",
            url: "/edit_items",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),

            success: function(){
                $("#title").val(""); // clears the textarea
                $("#author").val(""); // clears the textarea
                $("#summary").val(""); // clears the textarea
                $("#score").val(""); // clears the textarea
                $("#image").val(""); // clears the textarea
                $("#genres").val(""); // clears the textarea
                $("#series").val(""); // clears the textarea
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }

            
        });
        return true;
    }

}


$(document).ready(function(){
    //when the page loads, display all the names



    $('#searchForm').on('submit', function(e) { 
        e.preventDefault(); //prevent the form from submitting
        let searchTerm = $('#search').val().trim();
        if (searchTerm === '') {
            // If the search term is all whitespace, clear the search bar and set the focus back to it
            $('#search').val('').focus();
        } else {        
            window.location.href = '/search?q=' + encodeURIComponent(searchTerm); //redirect to the search page
        }
    });


    $('.item').click(function() {
        let itemId = $(this).data('id');
        window.location.href = '/view/' + encodeURIComponent(itemId); 
    });


    $.getJSON('/popular_items', function(items) {
        
        // Display the first 3 items
        // make this the top rated items 
        for (let i = 0; i < 10; i++) {

            if (i == 1 || i == 3 || i == 9 || i == 8) {
                let item = items[i];
                // console.log(item);
                let clippedSummary = item.summary.length > 150 ? item.summary.substring(0, 150) + '...' : item.summary;
                
                let itemHTML = `
                <a href="/view/${item.id}" class= "black no-underline">
                    <div class = "small-viewitem">
                                <img src="${item.image}" alt="${item.title} cover image" class = "small-float">
                                <div id = "small-container">
                                <div class = "search-main bold">${item.title}</div>
                                <div class = "font-small bottom-padding gray-dark">${item.author}</div>
                                <div><span class = "bold">Rating: </span> <span class = "orange">${item.score}</span></div>
                                <div class = "font-small gray-light"> ${clippedSummary}</div>
                                </div>
                    </div>
                </a>
                `; // Create the HTML for the item

                if (i == 1){
                    $('#searchResultsContainer').append(itemHTML); // Add the item to the search results container
                }
                if (i == 3){
                    $('#searchResultsContainer2').append(itemHTML); // Add the item to the search results container
                }
                if (i == 8){
                    $('#searchResultsContainer3').append(itemHTML); // Add the item to the search results container
                }
                if (i == 9){
                    $('#searchResultsContainer4').append(itemHTML); // Add the item to the search results container
                }
        }

    }
    });

    // add new data 
    
    $("#submit_book").click(function(){                
        get_and_save_book()
    }) 

    
    $("#series").keypress(function(e){     
        if(e.which == 13) {
            get_and_save_book()
        }   
    })

    $("#series2").keypress(function(e){     
        if(e.which == 13) {
            let url = window.location.pathname;
            let id = url.substring(url.lastIndexOf('/') + 1);
            if (edit_book(id)){
                window.location.href = '/view/' + id;
            }
        }   
    })


    $("#edit_book").click(function(){        
        let url = window.location.pathname;
        let id = url.substring(url.lastIndexOf('/') + 1);
        if (edit_book(id)){
            window.location.href = '/view/' + id;
        }
    }) 

    $("#discard_book").click(function(){
        
        let url = window.location.pathname;
        let id = url.substring(url.lastIndexOf('/') + 1);

        let confirmation = confirm("Are you sure you want to discard changes?");
        if (confirmation == true) {
            // Redirect to the view/<id> page
            window.location.href = '/view/' + id;
        } else {
            // Let them keep editing
            return false;
        }
    })


})