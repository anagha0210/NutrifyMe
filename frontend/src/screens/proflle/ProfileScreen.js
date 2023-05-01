import React, { useEffect, useState } from 'react'
import Button from 'screens/auth/components/Button'
import FormInput from 'screens/auth/components/FormInput'

import { SelectedIngredients } from 'shared/SelectedIngredient'
const ProfileScreen = () => {
  return (
    <div className='w-full min-h-screen bg-gray-50 flex flex-col lg:flex-row'>
      <IngredientScreen
        id='allergic'
        title={'Allergic ingredients'}
        subTitle='allergic'
      />
      <IngredientScreen
        id='favourite'
        title={'Favourite ingredients'}
        subTitle='favourite'
      />
    </div>
  )
}

const IngredientScreen = ({ id, title, subTitle }) => {
  const [ingredients, setIngredients] = useState([])

  const [inputIngredient, setInputIngredient] = useState('')
  const addIngredient = () => {
    if (inputIngredient) {
      const tempIngredients = [...ingredients, inputIngredient]
      setIngredients(tempIngredients)
    }
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

  const submitIngredients = () => {
    console.log('submit Ingredients ', ingredients)
    if (id === 'allergic') {
      // make axios request via allergic endpoint
    } else {
    }
  }

  return (
    <div className='w-full lg:w-[50%] lg:min-h-screen flex justify-center pt-8 p-2'>
      {/* all selected inputs */}

      <div className='flex flex-col gap-4'>
        <div>
          <p className='text-[20px] font-semibold'>{title}</p>
          <p>please input all of your {subTitle} ingredients one by one</p>
        </div>

        {/* added ingredients */}
        <div className='flex flex-col gap-2 mt-2'>
          <FormInput
            label='Enter Ingredient'
            type='text'
            value={inputIngredient}
            onChange={(e) => setInputIngredient(e.target.value)}
            placeholder='sugar...'
            required={true}
          />

          <Button title='Add' handleClick={addIngredient} />
        </div>

        <SelectedIngredients
          ingredients={ingredients}
          handleChange={handleChange}
          handleDelete={handleDelete}
        />
        <Button title='Submit' handleClick={submitIngredients} />
      </div>
    </div>
  )
}

export default ProfileScreen
