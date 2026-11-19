// shadcn/ui variant (shadcn studio "button-13"), kept as reference for React projects.
// In a shadcn project: `npx shadcn@latest add button` (plus lucide-react), then place this in
// components/shadcn-studio/button/ and adjust the '@/components/ui/button' import to match
// that project's components.json aliases.
import { Button } from '@/components/ui/button'
import { CopyIcon } from 'lucide-react'

const ButtonDuplicateDemo = () => {
  return (
    <Button
      variant='outline'
      className='border-sky-600 text-sky-600! hover:bg-sky-600/10 focus-visible:border-sky-600 focus-visible:ring-sky-600/20 dark:border-sky-400 dark:text-sky-400! dark:hover:bg-sky-400/10 dark:focus-visible:border-sky-400 dark:focus-visible:ring-sky-400/40'
    >
      <CopyIcon />
      Duplicate
    </Button>
  )
}

export default ButtonDuplicateDemo
