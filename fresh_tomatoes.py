#!/usr/bin/env python
print("content-type:text/html\n")
import webbrowser
import os
import re
main_page_head='''
<html lang="en">
<head>

<title>movie</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<div id="myModal" class="modal">

  <!-- Modal content -->
           <div class="modal-content">
                <span class="close">&times;</span>
                 <iframe id="f" width="560" height="315" src="" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
          </div>
          
</div>

   
   <script>
   // Get the modal
var modal = document.getElementById('myModal');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal 
    onc = function(c) {
    modal.style.display = "block";
    c='https://www.youtube.com/embed/'+c;
    console.log(c);
    document.getElementById("f").setAttribute("src",c);
}

// When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
} 

// When the user clicks anywhere outside of the modal, close it
   window.onclick = function(event) {
       if (event.target == modal) {
          modal.style.display = "none";
    } 
}
</script>
<style>

    .modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top:100px;
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content/Box */
.modal-content {
    margin: 5% auto; /* 5% from the top and centered */
    padding: 20px;
    width: 560px; /* Could be more or less, depending on screen size */
    min-height:500px;
}

/* The Close Button */
.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    background-color: black;
    text-decoration: none;
    cursor: pointer;
    padding-left:5px;
    padding-right:5px;
}
        .content {
            flex-wrap: wrap;
            display: flex;
            flex: 100%;
            justify-content: 100px;
	    background-color:green;
        }

        body {
            margin: 0;
        }

        h3 {
            color: white;
            background-color: black;
            height: 1.5cm;
            margin: 0px, 0px, 0px, 0px;
            text-align: center;
            font-size: 40px;
            font-family: 'Courgette', cursive;
        }
	 img 
	{
            height: 400px;
            width: 250px;



        }
        p{
            color: ghostwhite;
            text-align: center;
        }
      
        .king {
            padding-top: 15px;
            padding-left: 40px;
            padding-bottom: 30px;
            padding-right: 40px;
            background-color:rgb(255, 255, 255);
            width:260px;
            height: 432px;
            float: left;
           margin: 0.2cm;
        }

        .king:hover{
background-color: green;
        }

	
	

</style>

</head>
'''

main_page_content='''
<body>
    
   <h3> <center>Movie trailer</center></h3>

        <div>
            <div class="king" onclick="onc('ii_KxlHcm3A')">
               
		<img src="https://i.ytimg.com/vi/RmsVI_kEWO0/maxresdefault.jpg" ></a>

		<center><p><b>rouge</b></p>
                
            </div>
            <div class="king" onclick="onc('o-e5eWVCzx8')">
                   
                 <img src="https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Tamasha_%28film_poster%29.jpg/220px-Tamasha_%28film_poster%29.jpg"></a>

                        <p><b>tamasha</b></p>
                    
                </div>
                <div class="king" onclick="onc('vpfXFqlLA3A')">
                        <img src="https://upload.wikimedia.org/wikipedia/en/b/bc/Arya2_poster2.jpg"></a>
                        
                            <p><b>arya2</b></p>
                        
                    </div>
                    <div class="king" onclick="onc('KMWS5y2gZ6E')">
                        <img src="https://i3.behindwoods.com/telugu-movies/bharat-ane-nenu/stills-photos-pictures/thumbnails/bharat-ane-nenu-stills-photos-pictures-33.jpg"></a>
                        
                            <p><b>Bharath Ane Nenu</b></p>
                        
                    </div>
                    <div class="king" onclick="onc('mhhb6JAJKbE')">
                       <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2vntwFDoqLy0MRHlMXSgZTmu6iOc2n-3M4W2gosjcix7rFXwG"></a>
                        
                            <p><b>Rangasthalam</b></p>
                        
                    </div>
		 </div>

        <div>
      <!-- The Modal -->
         
</body>
'''

movie_title_content='''
<div class="col-md-6 col-lg-4 movie-title text-center" data-trailer=youtube-id="{trailer_youtube_id}" data-target="#trailer">
    <img src={poster_image_url}" width="220" height="324">
    <h2 style="color:white;">{movie_title}</h2>
</div>
'''

def create_movie_titles_content(movies):
    #the html content for this section of the page
    content = ''
    for movie in movies:
        #extract the youtube Id from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+',movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+',movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        #append the title for the movie with content filled in
        content += movie_title_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
            )
    return content
    
def open_movies_pages(movies):
    #create or overwrite the output file
    output_file = open('fresh_tomatoes.html','w')

    #Replace the movie titles placeholder generated content
    rendered_content = main_page_content.format(
        movie_titles = create_movie_titles_content(movies))

    #Output the file
    output_file.write(main_page_head+rendered_content)
    output_file.close()

    #open the output file in the browser(in a new tab,if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url,new=2)
            
