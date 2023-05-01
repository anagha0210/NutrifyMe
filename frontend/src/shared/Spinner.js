import React from 'react'

const Spinner = () => {
  return (
    <div className='w-full h-full flex flex-col gap-4 justify-center items-center'>
      <div className='animate-spin rounded-full h-12 w-12 border-b-4 border-gray-900'></div>
      <p className='text-[20px] text-black font-medium'>Loading...</p>
    </div>
  )
}

export default Spinner
