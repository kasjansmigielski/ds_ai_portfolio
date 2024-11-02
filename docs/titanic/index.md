# Eksploracja domenowa (EDA) zbioru danych: Titanic

*2024-08-27*

Zapraszam do zapoznania się z projektem mojego autorstwa, który przenosi nas w świat analizy danych dotyczących znanej całemu światu - katastrofy Titanic. W celu zgłębienia informacji wykorzystuję eksporację domenową (EDA). W tym projekcie znajdziesz mnóstwo trafnych wniosków i ciekawych obserwacji. Przygotuj się na ciekawą podróż z danymi, która poszerzy Twoje horyzonty patrzenia na jedną z największych katastrof morskich w historii.

<a href="titanic.ipynb" class="md-button md-button--primary">Pobierz Notebook</a>

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