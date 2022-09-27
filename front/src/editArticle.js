function makeEditionSectionAppears () {
    
    if (visibility == false) {
        visibility = true;
        editionSection.style.display = "flex";
        
    } else {
        visibility = false;
        editionSection.style.display = "none";
        cancelEdition();
    }    

}

function cancelEdition () {

    visibility = false;

    editionSection.style.display = "none";

    titleField.value = "Título";

    urlField.value = "URL"
}

// variables
let visibility = false;

// getting html elements
const editionButton = document.getElementById('edit-button');

const editionSection = document.getElementById("hidden-section");

const cancelButton = document.getElementById("cancel-button");

const titleField = document.getElementById("title-article-to-edit");

const urlField = document.getElementById("url-article-to-edit");

// listening events to make the edition section appears
editionButton.addEventListener('click', makeEditionSectionAppears);

cancelButton.addEventListener('click', cancelEdition);