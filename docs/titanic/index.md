# Domain exploration (EDA) of the dataset: Titanic

*Date of creation: 2024-08-25*

**Introduction:**<br>
I invite you to familiarize yourself with my project, which takes us into the world of data analysis regarding the world-famous Titanic disaster. In order to explore the information, I use domain exploration (EDA). In this project, you will find many relevant conclusions and interesting observations. Prepare yourself for an interesting journey with data that will broaden your horizons of looking at one of the greatest maritime disasters in history.

<a href="titanic.ipynb" class="md-button md-button--primary">Download Notebook</a>

<iframe
    id="content"
    src="titanic.html"
    width="100%"
    style="border:1px solid black;overflow:hidden;"
></iframe>
<script>
function resizeIframeToFitContent(iframe) {
    iframe.style.height = (iframe.contentWindow.document.documentElement.scrollHeight + 50) + "px";
    iframe.contentDocument.body.style["overflow"] = 'hidden';
}
window.addEventListener('load', function() {
    var iframe = document.getElementById('content');
    resizeIframeToFitContent(iframe);
});
window.addEventListener('resize', function() {
    var iframe = document.getElementById('content');
    resizeIframeToFitContent(iframe);
});
</script>