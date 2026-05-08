let download_links = document.querySelectorAll(".download_links")
console.log(download_links)
let base_massage = window.location.protocol+"//"+ window.location.host
async function copy_msg(id){
  let text = base_massage+"/download/"+id  
  try {
    await navigator.clipboard.writeText(text);
    alert('link copied to clipboard');
    return;
  } catch (err) {
    console.warn('Failed to copy: ', err);
  }
  // fall back incase clipboard doesnt work like if the srver is running on http 
  const textArea = document.createElement("textarea");
  textArea.value = text;
  textArea.style.position = "fixed"; 
  textArea.style.opacity = "0";
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  try {
    const successful = document.execCommand('copy');
    if (successful) alert('Link copied!');
    else throw new Error('execCommand returned false');
  } catch (err) {
    alert('copy failed:',err);
    console.error("Fallback failed:", err);
  }
}
for (let index = 0; index < download_links.length; index++) {
    const element = download_links[index];
    element.addEventListener("click",()=>{
        copy_msg(element.id)
    })
}