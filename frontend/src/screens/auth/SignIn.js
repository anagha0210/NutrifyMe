import React, { useState } from 'react'
import FormInput from './components/FormInput'
import { useNavigate } from 'react-router-dom'
import Button from './components/Button'

// api integration
import axiosClient from 'apiReq/axios'
import { ToastContainer, toast } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

const SignIn = ({ viewHandler, routeChange, setRouteChange }) => {
  const navigate = useNavigate()
  const [person, setPerson] = useState({
    emailAddress: '',
    password: '',
  })
  const handleChange = (e) => {
    setPerson({ ...person, [e.target.name]: e.target.value })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    axiosClient
      .post('signIn', person)
      .then((resp) => {
        toast.success('Login successfull', {
          position: toast.POSITION.TOP_RIGHT,
          autoClose: 3000,
        })
        localStorage.setItem('userData', JSON.stringify(resp?.data))
        setRouteChange(!routeChange)
        navigate('/home')
      })
      .catch(() => {
        toast.error('Invalid Credentials', {
          position: toast.POSITION.TOP_RIGHT,
          autoClose: 3000,
        })
      })
  }

  return (
    <section className='bg-gray-50 dark:bg-gray-900'>
      <div className='flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0 relative'>
      <img src="assets/siginbg.jpg" width='100%' className="absolute" />
        <div className='flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white z-10 '>
          <img
            className='w-8 h-8 mr-2'
            src='assets/omgfinally.png'
            alt='logo'
          />
          NutrifyMe- An Ingredient Analyzer Just For You!
        </div>
        <div className='w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700 z-10'>
          <div className='p-6 space-y-4 md:space-y-6 sm:p-8'>
            <h1 className='text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white'>
              Sign in to your account
            </h1>
            <form className='space-y-4 md:space-y-6' onSubmit={handleSubmit}>
              <FormInput
                label='email'
                type='email'
                name='emailAddress'
                value={person.emailAddress}
                onChange={handleChange}
                placeholder='name@company.com'
                required={true}
              />

              <FormInput
                label='password'
                type='password'
                name='password'
                value={person.password}
                onChange={handleChange}
                placeholder='••••••••'
                required={true}
              />

              <div className='flex items-center justify-between'>
                <div className='flex items-start'>
                  <div className='flex items-center h-5'>
                    <input
                      id='remember'
                      aria-describedby='remember'
                      type='checkbox'
                      className='w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800'
                      required=''
                    />
                  </div>
                  <div className='ml-3 text-sm'>
                    <label
                      htmlFor='remember'
                      className='text-gray-500 dark:text-gray-300'
                    >
                      Remember me
                    </label>
                  </div>
                </div>
              </div>
              <Button type='submit' title={'Sign in'} />
              <ToastContainer />

              <p className='text-sm font-light text-gray-500 dark:text-gray-400'>
                Don’t have an account yet?{' '}
                <button
                  className='font-medium text-primary-600 hover:underline dark:text-primary-500'
                  onClick={viewHandler}
                >
                  Sign up
                </button>
              </p>
            </form>
          </div>
        </div>
      </div>
    </section>
  )
}

export default SignIn
