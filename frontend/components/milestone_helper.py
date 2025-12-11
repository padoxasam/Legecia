from reactpy import html 
user_allowed_forma=["doc", "docx", "pdf", "txt", "rtf", "odt",
    "xls", "xlsx", "csv", "ppt", "pptx",
    "json", "xml", "zip", "7z", "tar", "gz",
    "mp4", "mov", "mkv", "avi", "mp3", "wav"]
bene_allowed_forma=["png", "jpg", "jpeg", "webp", "heic", "heif",
    "bmp", "tif", "tiff", "svg", "pdf",
    "mp4", "mov"]
def exit_of(filename:str)-> str:
    if not filename or '.' not in filename:
        return ''
    return filename.rsplit('.',1)[1].lower()
def validate_file_role(filename:str,role:str)->(bool.str):
    exit=exit_of(filename)
    if role == 'USER':
        ok=exit in user_allowed_forma
        allowed=', ' .join(sorted(user_allowed_forma))
    else:
        ok=exit in bene_allowed_forma
        allowed=', '.join(sorted(bene_allowed_forma))
    if ok:
        return True,''
    return False, f'Invalid File Type {exit} !\n Allowed are: {allowed}'
def filepreview(file_obj):
    name=getattr(file_obj,'name','file')
    url=getattr(file_obj,'url',None)
    if not url and exit_of(name) in ("png","jpg","jpeg","webp","bmp","tif","tiff","heic","heif"):
        return html.div({"style":{"padding":"8px","border":"1px dashed #ccc","borderRadius":"8px"}}, name)
    if url and exit_of(name) in ("png","jpg","jpeg","webp","bmp","tif","tiff","heic","heif"):
        return html.img({'src':url,'style':{"maxWidth":"200px","borderRadius":"8px"}})
    return html.div({"style":{"padding":"10px","background":"#299bb8","borderRadius":"6px"}}, name)