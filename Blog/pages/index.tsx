import type { NextPage } from 'next'
import Link from 'next/link'
const Home: NextPage = () => {
  return (
    <div>
      <h2>Hello World</h2>
      <Link href="/About"> about</Link>
    </div>
  )
}

export default Home
