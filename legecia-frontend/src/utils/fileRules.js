export const USER_ALLOWED = [
  "doc","docx","pdf","txt","rtf","odt",
  "xls","xlsx","csv","ppt","pptx",
  "json","xml","zip","7z","tar","gz",
  "mp4","mov","mkv","avi","mp3","wav"
]

export const BENE_ALLOWED = [
  "png","jpg","jpeg","webp","heic","heif",
  "bmp","tif","tiff","svg","pdf",
  "mp4","mov"
]

export function getExt(name){
  return name?.split(".").pop()?.toLowerCase() || ""
}

export function validateFile(name,role){
  const ext=getExt(name)
  const allowed=role==="USER"?USER_ALLOWED:BENE_ALLOWED
  if(!allowed.includes(ext)){
    throw new Error(`Invalid file type: ${ext}`)
  }
}
export function previewFile(file){
  const ext=getExt(file.name)
  if(["png","jpg","jpeg","webp"].includes(ext)){
    return URL.createObjectURL(file)
  }
  return null
}
