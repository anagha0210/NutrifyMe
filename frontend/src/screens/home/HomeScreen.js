import React, { useEffect, useState } from 'react'
import { createWorker } from 'tesseract.js'
import { SelectedIngredients } from 'shared/SelectedIngredient'
import Button from 'screens/auth/components/Button'
import Tesseract from 'tesseract.js'
import Spinner from 'shared/Spinner'
const HomeScreen = () => {
  const [ingredients, setIngredients] = useState([])

  const extractIngredients = (ocrText) => {
    setIngredients(ocrText.split(' '))
  }

  const handleChange = (index, value) => {
    let tempList = ingredients.map((ingredient, idx) => {
      if (idx === index) {
        return value
      } else return ingredient
    })

    setIngredients(tempList)
  }

  const handleDelete = (index) => {
    let tempList = [...ingredients]

    tempList.splice(index, 1)
    setIngredients([...tempList])
  }
  const getRecommendations = () => {}

  return (
    <div className='w-full min-h-screen bg-gray-50 flex flex-col items-center'>
      <div className='w-[80%] flex flex-col gap-4'>
        <div>
          <p className='text-[20px] font-semibold'>
            Ingredient Recommender System
          </p>
          <p>We recommend food on the basis of your food profile</p>
        </div>
        <div className='w-[400px] h-full flex flex-col gap-2'>
          <ImageToText extractIngredients={extractIngredients} />
          <SelectedIngredients
            ingredients={ingredients}
            handleChange={handleChange}
            handleDelete={handleDelete}
          />
          <Button title='Submit' handleClick={getRecommendations} />
        </div>
      </div>
    </div>
  )
}

const ImageToText = ({ extractIngredients }) => {
  const [ocr, setOcr] = useState('')
  const [imageData, setImageData] = useState(null)
  const [loading, setLoading] = useState(false)

  const convertImageToText = async () => {
    if (!imageData) return
    setOcr('')
    setLoading(true)
    Tesseract.recognize(
      imageData,
      'eng',
      { logger: (m) => console.log(m) }
    )
      .then(({ data: { text } }) => {
        setOcr(text)
        extractIngredients(text)
        setLoading(false)

        console.log('tessareact response is', text)
      })
      .catch((err) => {
        setLoading(false)
      })
  }

  useEffect(() => {
    convertImageToText()
  }, [imageData])

  function handleImageChange(e) {
    const file = e.target.files[0]
    if (!file) return
    const reader = new FileReader()
    reader.onloadend = () => {
      const imageDataUri = reader.result
      console.log({ imageDataUri })
      setImageData(imageDataUri)
    }
    reader.readAsDataURL(file)
  }
  return (
    <div className=''>
      <div>
        <p>Choose an Image</p>
        <input
          type='file'
          name=''
          id=''
          onChange={handleImageChange}
          accept='image/*'
        />
      </div>
      <div className='w-full'>
        {imageData && (
          <img
            className='w-full h-[300px] bg-red-100 rounded-[12px] object-contain flex flex-col mt-2'
            src={imageData}
            alt=''
            srcSet=''
          />
        )}
      </div>

      {loading ? (
        <div className='w-full h-40'>
          <Spinner />
        </div>
      ) : (
        <div className='w-full text-black mt-2'>
          <p>{ocr}</p>
        </div>
      )}
    </div>
  )
}

export default HomeScreen
